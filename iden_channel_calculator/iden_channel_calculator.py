#!/usr/bin/python
# -*- coding: utf-8 -*-


class IDENChannelCalculator:
    """
    iDEN channel information calculator

    :param base: base frequency (Hz)
    :param spacing: channel spacing (Hz)
    :param offset: RX offset (Hz)
    :param bandwidth: channel bandwidth (Hz)
    """

    def __init__(
        self,
        base: int,
        spacing: int,
        offset: int,
        bandwidth: int,
    ) -> None:
        self.base = base
        self.spacing = spacing
        self.offset = offset
        self.bandwidth = bandwidth

    def get_channel_number_by_frequency(self, transmit_frequency: int) -> int:
        """
        get the iDEN channel's channel number by its frequency

        :param transmit_frequency: the frequency to calculate the channel number from
        :return: the channel's channel number as int, -1 when frequency is invalid
        """
        channel_number = (transmit_frequency - self.base) / self.spacing
        if channel_number.is_integer():
            return int(channel_number)
        return -1

    def get_frequency_by_channel_number(self, channel_number: int) -> int:
        """
        get the iDEN channel's frequency given its channel number

        :param channel_number: the channel number to calculate the frequency from
        :return: the channel's frequency in Hz
        """
        return self.base + channel_number * self.spacing
