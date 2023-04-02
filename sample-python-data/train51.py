def fit_opt_sched(self, phases, cycle_save_name=None, best_save_name=None, stop_div=False, data_list=None, callbacks=None, 
                      cut = None, use_swa=False, swa_start=1, swa_eval_freq=5, **kwargs):
        """Wraps us the content of phases to send them to model.fit(..)

        This will split the training in several parts, each with their own learning rates/
        wds/momentums/optimizer detailed in phases.

        Additionaly we can add a list of different data objets in data_list to train
        on different datasets (to change the size for instance) for each of these groups.

        Args:
            phases: a list of TrainingPhase objects
            stop_div: when True, stops the training if the loss goes too high
            data_list: a list of different Data objects.
            kwargs: other arguments
            use_swa (bool, optional): when this is set to True, it will enable the use of
                Stochastic Weight Averaging (https://arxiv.org/abs/1803.05407). The learner will
                include an additional model (in the swa_model attribute) for keeping track of the 
                average weights as described in the paper. All testing of this technique so far has
                been in image classification, so use in other contexts is not guaranteed to work. 
            swa_start (int, optional): if use_swa is set to True, then this determines the epoch
                to start keeping track of the average weights. It is 1-indexed per the paper's
                conventions.
            swa_eval_freq (int, optional): if use_swa is set to True, this determines the frequency
                at which to evaluate the performance of the swa_model. This evaluation can be costly
                for models using BatchNorm (requiring a full pass through the data), which is why the
                default is not to evaluate after each epoch.
        Returns:
            None
        """
        if data_list is None: data_list=[]
        if callbacks is None: callbacks=[]
        layer_opt = LayerOptimizer(phases[0].opt_fn, self.get_layer_groups(), 1e-2, phases[0].wds)
        if len(data_list) == 0: nb_batches = [len(self.data.trn_dl)] * len(phases)
        else: nb_batches = [len(data.trn_dl) for data in data_list] 
        self.sched = OptimScheduler(layer_opt, phases, nb_batches, stop_div)
        callbacks.append(self.sched)
        metrics = self.metrics
        if best_save_name is not None:
            callbacks+=[SaveBestModel(self, layer_opt, metrics, best_save_name)]
        if use_swa:
            # make a copy of the model to track average weights
            self.swa_model = copy.deepcopy(self.model)
            callbacks+=[SWA(self.model, self.swa_model, swa_start)]
        n_epochs = [phase.epochs for phase in phases] if cut is None else cut
        if len(data_list)==0: data_list = [self.data]
        return fit(self.model, data_list, n_epochs,layer_opt, self.crit,
            metrics=metrics, callbacks=callbacks, reg_fn=self.reg_fn, clip=self.clip, fp16=self.fp16,
            swa_model=self.swa_model if use_swa else None, swa_start=swa_start, 
            swa_eval_freq=swa_eval_freq, **kwargs)