#!/usr/bin/python
# -*- coding: utf-8 -*-


class IDENChannelCalculator:
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
        channel_number = (transmit_frequency - self.base) / self.spacing
        if channel_number.is_integer():
            return int(channel_number)
        return False

    def get_frequency_by_channel_number(self, channel_number: int) -> int:
        return self.base + channel_number * self.spacing
