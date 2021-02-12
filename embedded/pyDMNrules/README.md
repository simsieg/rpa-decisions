# pyDMNrules Setup

[pyDMNrules](https://pypi.org/project/pyDMNrules/) currently only supports one decision output result for multi-hit policies due to a software bug.

Therefore a patch for pyDMNrules was developed.

## Installing pyDMNrules

Install pyDMNrules via pip3.

``` 
pip3 install pyDMNrules
```

## Patching pyDMNrules

To patch pyDMNrules, two approaches are possible:

### Applying the DMNrules.patch

1. Navigate to the pyDMNrules folder in your python dist-packages directory, where the `DMNrules.py` file is located.
For example:

```bash
cd /usr/local/lib/python3.8/dist-packages/pyDMNrules
```

2. Copy or download the [DMNrules.patch](./DMNrules.patch) file into this directory.

```bash
wget https://raw.githubusercontent.com/simsieg/rpa-decisions/master/embedded/pyDMNrules/DMNrules.patch
```

3. Apply the patch

```bash
patch --verbose --unified DMNrules.py < DMNrules.patch
```

### Replace the DMNrules.py File

Alternatively, you can replace the `DMNrules.py` file  in your python dist-packages directory with the patched file version available [here](./DMNrules.py).
