# -*- coding: utf-8 -*-

"""Classes for creating and persisting (fitted) ML models."""

import joblib


class Model:
    """Base class representing a basic model.

    This class defines a generic interface for a machine learning model, which consists
    of a single `fit` method. Implementations of `fit` should take care of fitting
    the model on a specific dataset and return a `ModelFit` instance, which represents
    a read-only model fit that can be used to perform predictions and can be persisted.
    """

    def fit(self, X, y):
        """
        Fits model on given dataset.

        Parameters
        ----------
        X : pd.Dataframe
            Dataframe containing training data (features only, no response).
        y : Union[pd.Series, np.ndarray]
            Pandas series (or numpy array) containing the response values for the
            given training dataset.

        Returns
        -------
        Model
            Returns the model itself, after fitting.
        """
        return self

    def predict(self, X):
        """
        Produces predictions for the given dataset.

        Parameters
        ----------
        X : pd.DataFrame
            Dataframe to produce predictions for.
        """
        raise NotImplementedError()

    @classmethod
    def load(cls, file_path):
        """Loads model fit from given file path.

        Parameters
        ----------
        file_path : str
            Path to a pickled model file.

        Returns
        -------
        ModelFit
            The unpickled model instance.

        """
        return joblib.load(file_path)

    def save(self, file_path):
        """Saves model fit to given file path.

        Parameters
        ----------
        file_path : str
            Path to save the pickled model to.

        """
        joblib.dump(self, file_path)


class TitanicModel(Model):
    """A RandomForest-based model for predicting survival in the Titanic dataset."""

    # TODO: Implement Titanic model in sklearn (preferably as a sklearn Pipeline).
    #   See https://bit.ly/2UTUaoe for more details on Pipelines.
    #   Tip: use the sklearn Column transformer to transform pandas DataFrames.

    def fit(self, X, y):
        # TODO: Implement fit.
        raise NotImplementedError()

    def predict(self, X):
        # TODO: Implement predict.
        raise NotImplementedError()
