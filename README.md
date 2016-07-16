# simple-engine

`simple-engine` reads in an html file and generates a JSON map corresponding to the html.

## usage

put a `config.json` file in a place that makes it convenient to type the source and destination paths out (a root
directory will do)

ex. `config.json`

    {
        "src": "app/index.html",
        "dest": "output.js",
        "toplevelid": "start"
    }

then run `engine` from the command line.

### options

| option | description | default |
| :----: | :---------: | :----: |
| `src` | source html file | `index.html` |
| `dest` | destination file | `simpleDom.js` |
| `toplevelid` | html id where the interpreter starts | `start` |

