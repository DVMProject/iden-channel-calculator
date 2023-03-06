#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import traceback

from .iden_channel_calculator import IDENChannelCalculator


def parse_arguments() -> argparse.Namespace:
    """
    parse command line arguments

    :rtype argparse.Namespace: command parsing results
    """
    parser = argparse.ArgumentParser(
        prog="iden-channel-calculator",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-b", "--base", type=int, help="base frequency (Hz)", required=True
    )
    parser.add_argument(
        "-s",
        "--spacing",
        type=float,
        help="channel spacing (kHz)",
        default=6.25,
    )
    parser.add_argument(
        "-o", "--offset", type=float, help="input offset (MHz)", default=5.0
    )
    parser.add_argument(
        "-w", "--bandwidth", type=float, help="channel bandwidth (kHz)", default=12.5
    )
    parser.add_argument("-i", "--channel-id", type=int, help="channel ID", default=0)

    # the user must provide either the TX frequency or the ChNo
    given = parser.add_mutually_exclusive_group(required=True)
    given.add_argument(
        "-t", "--transmit-frequency", type=int, help="transmit frequency"
    )
    given.add_argument(
        "-c", "--channel-number", type=lambda x: int(x, 16), help="channel number (hex)"
    )
    return parser.parse_args()


def main() -> int:
    """
    command line entrypoint for direct CLI invocation

    :rtype int: 0 if completed successfully, else other int
    """

    try:
        # parse command line arguments
        args = parse_arguments()

        # convert all values into Hz
        spacing = int(args.spacing * 10**3)
        offset = int(args.offset * 10**6)
        bandwidth = int(args.bandwidth * 10**3)

        calculator = IDENChannelCalculator(args.base, spacing, offset, bandwidth)

        # both channel_number and transmit_frequency are guaranteed to be present
        #   because they are requried in a mutually exclusive group in argparse
        # calculate the channel number if it is not provided
        if args.channel_number is None:
            args.channel_number = calculator.get_channel_number_by_frequency(
                args.transmit_frequency
            )
        # calculate the transmit frequency if it is not provided
        if args.transmit_frequency is None:
            args.transmit_frequency = calculator.get_frequency_by_channel_number(
                args.channel_number
            )

        # if the given frequency doesn't match any channel number
        if args.channel_number is False:
            print("Error: invalid transmit frequency specified", file=sys.stderr)
            return 1

        summary = {
            "Base Frequency (Hz)": args.base,
            "Channel Spacing (kHz)": args.spacing,
            "Receive Offset (MHz)": args.offset,
            "Channel Bandwidth (kHz)": args.bandwidth,
            "Transmit Frequency (Hz)": args.transmit_frequency,
            "Receive Frequency (Hz)": args.transmit_frequency + offset,
            "Channel Number (hex)": hex(args.channel_number),
            "iDEN Table Line": "{},{},{},{},{},".format(
                args.channel_id, args.base, args.spacing, args.offset, args.bandwidth
            ),
        }

        # print all of the fields
        for key, value in summary.items():
            print(
                "{0:{minimum_width}}{1}".format(
                    key + ": ",
                    value,
                    minimum_width=max([len(length) for length in list(summary)]) + 3,
                )
            )

    # don't print the traceback for manual terminations
    except KeyboardInterrupt:
        return 2

    except Exception as error:
        traceback.print_exc(error)
        return 1

    # if no exceptions were produced
    else:
        return 0


if __name__ == "__main__":
    sys.exit(main())
