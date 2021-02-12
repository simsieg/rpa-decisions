# Automagica Installation

Since Automagica was removed from the pip repository, some efforts are required to get Automagica running.

## Installation from Old Git Commit

Make sure `python3.8` and `python3-setuptools` are installed on your system.
Then run the following commands.

```bash
apt-get update -y
apt-get upgrade -y
apt-get install python3-setuptools -y
git clone https://github.com/automagica/automagica
cd automagica
git checkout d550012993104f71de6cce53fcc2f2b46900050a
pip install -e .
```

## Extending Automagica with Decision Capabilities

To adapt Automagica to work with the newly created decision tasks, replace the dist-package activities.py file of your Automagica installation with the patched one avaiable in this repository.

To do so, replace (or similar depending on your system)

`/usr/local/lib/python3.8/dist-packages/automagica/activities.py`

with

[`activities.py`](./activities.py)

After this, your Automagica software version can execute new decision tasks.

## Running

Automagica can be started by executing:

`automagica flow new`

When Automagica was extended correctly, three decision tasks (*Internal decision engine*, *Camunda decision service*, and *Human decision*) should be visible in the Automagica user interface like in this screenshot:

![Automagica UI](./img/extended-automagica-ui.png "Automagica user interface with decision tasks")

