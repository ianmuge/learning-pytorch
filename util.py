
def render_sample_data(data):
    import matplotlib.pyplot as plt
    n=len(data)
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(data[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()
def render_data(data):
    import matplotlib.pyplot as plt
    plt.imshow(data.reshape(28, 28))
    plt.gray()
    plt.show()