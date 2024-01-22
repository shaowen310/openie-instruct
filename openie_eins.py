import argparse
import logging
from instruct import IEPrompt

logger = logging.getLogger(__file__)


def argparser():
    ap = argparse.ArgumentParser("Easy instruction for OpenIE.")

    ap.add_argument(
        "--input_file",
        required=True,
        type=str,
        help="Input sentences.",
    )
    ap.add_argument(
        "--output_file",
        required=True,
        type=str,
        help="Output extractions.",
    )

    return ap


def main(args):
    logger.info(f"Input file: {args.input_file}")

    ie_prompter = IEPrompt("rte")

    # if not args.zero_shot:
    #     examples = prepare_examples(args.data_path, args.task, args.language)

    with open(args.input_file, "r") as infile:
        for sentence in infile:
            ie_prompter.build_prompt(
                prompt=sentence,
                language="en",
                in_context=False,
            )

            result = ie_prompter.get_openai_result()

    logger.info(result)


if __name__ == "__main__":
    ap = argparser()
    args = ap.parse_args()

    main(args)
