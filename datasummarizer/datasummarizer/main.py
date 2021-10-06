"""Define the command-line interface for the datasummarizer program."""

# TODO: import the Path object from the pathlib module

# TODO: import the type module

# TODO: import the summarize module from datasummarizer

# TODO: import the transform module from datasummarizer

# TODO: import the Console object from the rich.console

cli = typer.Typer()

console = Console()


@cli.command()
def main(
    data_file: Path = typer.Option(...),
):
    """Summarize the data values stored in a file."""
    # display details about the file provided on the command line
    data_text = ""
    # --> the file was not specified so we cannot continue using program
    if data_file is None:
        console.print("No data file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if data_file.is_file():
        data_text = data_file.read_text()
        data_line_count = len(data_text.splitlines())
        console.print(
            f":microscope: The data file contains {data_line_count} data values in it! Let's get summarizing!"
        )
        console.print()
        # transform the data from a list of textual values to a list of numerical values
        data_list = transform.transform_string_to_number_list(data_text)
        # compute the mean from the list of numerical values
        computed_mean = summarize.compute_mean(data_list)
        # display the computed mean in the terminal window
        console.print(f":abacus: The computed mean is {computed_mean}!")
    # --> the file was specified but it does not exist so we cannot continue using program
    elif not data_file.exists():
        console.print("The data file does not exist!")
