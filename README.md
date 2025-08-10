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

## License
See LICENSE file.
