from flask import Flask

app = Flask(__name__)


def do_nothing():
    """
    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is
        False)

    Returns
    -------
    list
        a list of strings used that are the header columns
    """

    pass


def super_fonction(input_1: str, *args, **kwargs) -> str:

    """
    Super Fonction va sauver le monde.

    Appelez super fonction en cas de désastre nucléaire, elle ne fera rien.

    Parameters
    ----------
    input_1 : str
        ce paramètre ne sert à rien
    args : list, optional
        cette liste de paramètres ne sert à rien
    kwargs : array_like, optional
            ce dictionnaire de paramètres ne sert à rien

     Returns
    -------
    string
        always returns 'super fonction a encore frappé.'
    """

    for value in args:
        do_nothing()

    for key, value in kwargs.items():
        do_nothing()

    return "super fonction a encore saoulé"


@app.route('/')
def hello_world():
    return "<h1>L'app flask fonctionne dans le container docker</h2>"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
