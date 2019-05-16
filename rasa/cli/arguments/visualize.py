import argparse

from rasa.cli.arguments.default_arguments import (
    add_config_param,
    add_domain_param,
    add_stories_param,
    add_out_param,
)


def set_visualize_stories_arguments(parser: argparse.ArgumentParser):
    add_domain_param(parser)
    add_stories_param(parser)
    add_config_param(parser)

    add_out_param(
        parser,
        default="graph.html",
        help="Filename of the output path, e.g. 'graph.html'.",
    )

    parser.add_argument(
        "--max-history",
        default=2,
        type=int,
        help="Max history to consider when merging paths in the output graph.",
    )

    parser.add_argument(
        "-u",
        "--nlu",
        default=None,
        type=str,
        help="File or folder containing your NLU data, "
        "used to insert example messages into the graph.",
    )
