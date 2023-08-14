import os
import click

VALID_FORMATS = ['.csv', '.txt']

def validate_output_paths(_ctx, _param, paths):
    """Verify that the extension of each output file path corresponds to a known
          output format, and return a dictionary mapping the path
          to its format."""
    def get_format_from_path(path):
        _base, extension = os.path.splitext(path)
        return extension.lower()

    output_spec = {}
    for path in paths:
        format = get_format_from_path(path)
        if format not in VALID_FORMATS:
            raise click.BadParameter(f"Output file {path} has an invalid format {format}. Known formats are {', '.join(VALID_FORMATS)}.")
        output_spec[path] = format

    return output_spec


@click.command(no_args_is_help=True)
@click.option("--number", default=10, type=click.IntRange(min=1),
              help="Maximum number of frequent words to include")
@click.option("--output", "output_spec", required=True, multiple=True, type=click.Path(),
              callback=validate_output_paths,
              help="Path of an output file. The extension (.txt or .csv) determines the output format.")
@click.argument("input_paths", required=True, type=click.Path(exists=True), nargs=-1)
def main(number, output_spec, input_paths):
    """Main entry point of the console application."""

    #TODO add some of your code here
    # Remember to structure and package your code and tests appropriately.
    # Do not just add _all_ your code here.

    pass


if __name__ == '__main__':
    main()
