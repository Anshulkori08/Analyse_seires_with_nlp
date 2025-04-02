from sklearn.utils.class_weight import compute_class_weight
import numpy as np
import torch
import evaluate

metric = evaluate.load('accuracy')
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

import numpy as np  # Add this import at the top of the file

def get_class_weights(data):
    """Calculate class weights for imbalanced datasets."""
    labels = data['label'].tolist()
    unique_classes = np.unique(labels)  # This returns a numpy array
    class_weights = compute_class_weight(
        class_weight="balanced",
        classes=unique_classes,  # Now passing a numpy array
        y=labels
    )
    return torch.tensor(class_weights, dtype=torch.float32)
