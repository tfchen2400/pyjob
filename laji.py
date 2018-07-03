def label_func(df, label_values, label_name="label"):
    import tensorflow as tf
    label_values = label_values - df['close']
    label_values[label_values > 0] = 1
    label_values[label_values <= 0] = 0
    df[label_name] = label_values
    return df