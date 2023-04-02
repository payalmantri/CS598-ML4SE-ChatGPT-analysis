def lr_find2(self, start_lr=1e-5, end_lr=10, num_it = 100, wds=None, linear=False, stop_dv=True, **kwargs):
        """A variant of lr_find() that helps find the best learning rate. It doesn't do
        an epoch but a fixed num of iterations (which may be more or less than an epoch
        depending on your data).
        At each step, it computes the validation loss and the metrics on the next
        batch of the validation data, so it's slower than lr_find().

        Args:
            start_lr (float/numpy array) : Passing in a numpy array allows you
                to specify learning rates for a learner's layer_groups
            end_lr (float) : The maximum learning rate to try.
            num_it : the number of iterations you want it to run
            wds (iterable/float)
            stop_dv : stops (or not) when the losses starts to explode.
        """
        self.save('tmp')
        layer_opt = self.get_layer_opt(start_lr, wds)
        self.sched = LR_Finder2(layer_opt, num_it, end_lr, linear=linear, metrics=self.metrics, stop_dv=stop_dv)
        self.fit_gen(self.model, self.data, layer_opt, num_it//len(self.data.trn_dl) + 1, all_val=True, **kwargs)
        self.load('tmp')