
> **⚠️ This project is under active development and is not production-ready. Use at your own risk.**

# ExperimentalGraphToolkit



## Features
- Loading and preprocessing data from CSV, Excel, JSON
- Flexible architecture for adding new types of plots and data processing
- Configuration via `config.json` file

## Quick Start
1. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. Configure `config.json` for your data and desired plot type.
3. Run:
   ```bash
   python main.py
   ```

## Project Structure
- `main.py` — main control script
- `plot_types/` — modules for different plot types
- `data_processing/` — modules for loading and preprocessing data
- `config.json` — configuration file


## Working with Templates
You can save processing and plotting templates in the `templates/` folder as separate JSON files. In `config.json`, specify the `"template"` field with the template name, for example:

```
{
   "template": "lineplot_template.json",
   "data_path": "data/your_data.csv"
}
```

All parameters from the template will be used by default. If there are fields in `config.json` that overlap with the template, the values from the template take precedence and override the config.json values.

This allows you to quickly switch between different processing scenarios and build plots using saved patterns, while flexibly customizing individual parameters for each run.

## License
See LICENSE file.
