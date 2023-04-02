def predict_array(self, arr):
        """
        Args:
            arr: a numpy array to be used as input to the model for prediction purposes
        Returns:
            a numpy array containing the predictions from the model
        """
        if not isinstance(arr, np.ndarray): raise OSError(f'Not valid numpy array')
        self.model.eval()
        return to_np(self.model(to_gpu(V(T(arr)))))