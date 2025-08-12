

import json
import importlib
import pkgutil
import plot_types
import data_processing

# Automatic formation of plot_functions
plot_functions = {}
for loader, module_name, is_pkg in pkgutil.iter_modules(plot_types.__path__):
    module = importlib.import_module(f'plot_types.{module_name}')
    if hasattr(module, 'process_and_plot'):
        plot_functions[module_name] = module.process_and_plot

# Automatic formation of data_loaders
data_loaders = {}
for loader, module_name, is_pkg in pkgutil.iter_modules(data_processing.__path__):
    module = importlib.import_module(f'data_processing.{module_name}')
    if hasattr(module, 'load_and_preprocess'):
    # Key - filename without data_loader_ (e.g., csv, excel, json)
        key = module_name.replace('data_loader_', '')
        data_loaders[key] = module.load_and_preprocess

def main():
    with open('config.json', encoding='utf-8') as f:
        config = json.load(f)

    # If template is specified, load parameters from template file
    template_name = config.get('template')
    if template_name:
        template_path = f'templates/{template_name}'
        try:
            with open(template_path, encoding='utf-8') as tf:
                template = json.load(tf)
            # Merge template into config (template values override config)
            config = {**config, **template}
        except Exception as e:
            print(f'Failed to load template: {e}')
            return

    data_type = config.get('data_type')
    data_path = config.get('data_path')
    plot_type = config.get('plot_type')
    plot_params = config.get('plot_params', {})

    loader = data_loaders.get(data_type)
    if not loader:
        print('Unknown data type')
        return
    data = loader(data_path)

    plot_func = plot_functions.get(plot_type)
    if not plot_func:
        print('Unknown plot type')
        return
    plot_func(data, **plot_params)

if __name__ == '__main__':
    main()
