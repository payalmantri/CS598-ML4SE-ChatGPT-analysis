def TTA(self, n_aug=4, is_test=False):
        """ Predict with Test Time Augmentation (TTA)

        Additional to the original test/validation images, apply image augmentation to them
        (just like for training images) and calculate the mean of predictions. The intent
        is to increase the accuracy of predictions by examining the images using multiple
        perspectives.


            n_aug: a number of augmentation images to use per original image
            is_test: indicate to use test images; otherwise use validation images

        Returns:
            (tuple): a tuple containing:

                log predictions (numpy.ndarray): log predictions (i.e. `np.exp(log_preds)` will return probabilities)
                targs (numpy.ndarray): target values when `is_test==False`; zeros otherwise.
        """
        dl1 = self.data.test_dl     if is_test else self.data.val_dl
        dl2 = self.data.test_aug_dl if is_test else self.data.aug_dl
        preds1,targs = predict_with_targs(self.model, dl1)
        preds1 = [preds1]*math.ceil(n_aug/4)
        preds2 = [predict_with_targs(self.model, dl2)[0] for i in tqdm(range(n_aug), leave=False)]
        return np.stack(preds1+preds2), targs