# system_prompts extension

This extension allows configuring System Prompts in the `llms` UI.

![](https://llmspy.org/img/ext/system_prompts.png)

## Install

This extension can be installed with:

```bash
llms --add system_prompts
```

## Uninstall

This extension can be removed with:

```bash
llms --remove system_prompts
```

## Custom User Prompts

This extension also searches for `prompts.json` in the user's home directory.

If signed in (e.g. via GitHub OAuth), it first looks in:

    ~/.llms/user/<user>/system_prompts/prompts.json

Otherwise it looks in the default user location:

    ~/.llms/user/default/system_prompts/prompts.json

If neither exists, it defaults to the `ui/prompts.json` included in this extension.

### Example `prompts.json`

```json
[
    {
        "name": "Vue Developer",
        "prompt": "You are an expert Vue developer..."
    },
    {
        "name": "Python Expert",
        "prompt": "You are an expert Python developer..."
    }
]
```
