# EOD

A python script for generating a daily summary from my [Toggl Track](https://www.toggl.com/) entries
using the [Toggl API v8](https://github.com/toggl/toggl_api_docs/blob/master/toggl_api.md).

## Setup

You can make the file available on the command link by adding a Symlink in your /usr/local/bin 
directory. The following is an example making it available as `eod`

```shell
ln -s /path/to/project/app.py /usr/local/bin/eod
```

You'll also need to export your API Token to from [your Toggl Track profile](https://track.toggl.com/profile)
as `TOGGLE_KEY` to use this.
