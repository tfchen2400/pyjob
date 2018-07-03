def parse_function(example, **kwargs):
    import tensorflow as tf
    features = tf.parse_single_example(
        example,
            features={
                'label': tf.FixedLenFeature([], tf.int64),
                'image_raw': tf.FixedLenFeature([], tf.string)
            })
    image = tf.decode_raw(features['image_raw'], tf.uint8)
    image = tf.decode_raw(features['image_raw'], tf.uint8)
    image_shape = tf.stack([28, 28, 4])
    image = tf.reshape(image, image_shape)
    return image, label


    import tensorflow as tf
    features = tf.parse_single_example(
        example,
        features={
            'label': tf.FixedLenFeature([], tf.int64),
            'image_raw': tf.FixedLenFeature([], tf.string)
        })
    image = tf.decode_raw(features['image_raw'], tf.uint8)
    image = tf.decode_raw(features['image_raw'], tf.uint8)
    image_shape = tf.stack([28, 28, 4])
    image = tf.reshape(image, image_shape)
    return image, label



