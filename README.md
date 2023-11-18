# alxcheck

ALX test Suite. Shell Utility that checks for ALX Project Requirements

## Dependencies

- [`Python3`](https://www.python.org/downloads/)
- [`betty`](https://youtu.be/wDDKOOEPED0?ref=alxcheck)
- [`pycodestyle`](https://pycodestyle.pycqa.org/en/latest/)
- [`semistandard`](https://www.npmjs.com/package/semistandard)

## Features

`alxcheck` checks for the following:

### General

- `README.md` file present.
- `README.md` file is not empty.
- All files in the current folder and sub-folders end with a new line.

### C

- runs `betty` check.
  > Note: You would have to make sure betty is installed. Check out [How To Install Betty](https://youtu.be/wDDKOOEPED0?ref=alxcheck)

### Python

- Python file is executable.
- *shebang* is present and at the top of the file (`#!/usr/bin/python3` or `#!/usr/bin/env python3`)
- Module documentation (docstrings)
- Function documentation (docstrings)
- Class documentation (docstrings)

### JavaScript

- Javascript file is executable
  > Note: enabled with `-js` or `--nodejs-project` command line switch. See [Usage](#usage) below
- *shebang* is present and at the top of the file (`#!/usr/bin/node` or `#!/usr/bin/env node`)
  > Note: enabled with `-js` or `--nodejs-project` command line switch. See [Usage](#usage) below
- `semistandard` check
  > Note: you would have to install semistandard `npm install semistandard -g`
- `var` is not used.

## Installation

```bash
pip install alxcheck
```

or

```bash
python3 -m pip install alxcheck
```

## Usage

After installation, to use this package, just run it as a shell command. This starts the checks with the current working directory as the root of the project.

```bash
alxcheck
```

If the project is a JavaScript project with node.js scripts, a command line switch can be used to enable the first two checks [listed above](#javascript).

```bash
alxcheck -js #shorthand version
```

or

```bash
alxcheck --nodejs-project #long version
```

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback is valuable!

## License

This project is licensed under the [MIT License](./LICENSE).
