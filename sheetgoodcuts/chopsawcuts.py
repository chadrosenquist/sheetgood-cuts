"""Provides APIs to optimally cut wood with your chop (miter) saw."""

from sheetgoodcuts import Mixed, QuantityBoard, Board, BoardResult


class ChopSawCuts(object):
    SAW_BLADE_WIDTH = "1/8"
    EXCESS_PER_CUT = "2"

    def __init__(self,
                 desired_cuts,
                 available_boards,
                 saw_blade_width=SAW_BLADE_WIDTH,
                 excess_per_cut=EXCESS_PER_CUT):
        """
        :param desired_cuts: List of desired cuts.  Each item must be a Board or a QuantityBoard.
        :param available_boards: List of available boards.  Each item must be a Board or a QuantityBoard.
        :param saw_blade_width: Width of the saw blade.  Defaults to 1/8".
        :param excess_per_cut: Excess material per cut.  Defaults to 2".
        """
        self.saw_blade_width = Mixed(saw_blade_width)
        self.excess_per_cut = Mixed(excess_per_cut)
        self.desired_cuts = self._convert_quantityboard_to_board_list("desired_cuts", desired_cuts)
        self.available_boards = self._convert_quantityboard_to_board_list("available_boards", available_boards)
        #for cut in self.desired_cuts:
        #    print(cut)

    @staticmethod
    def _convert_quantityboard_to_board_list(parameter_name,
                                             desired_cuts):
        """Converts the cuts to a list.

        :param parameter_name: Name of the parameter to display in case of error.
        :param desired_cuts: The list must consist of either QuantityBoard's or Board's.
        :return: List of boards, only containing the Board object.
        """
        return_value = []
        for cut in desired_cuts:
            if isinstance(cut, QuantityBoard):
                for count in range(cut.quantity):
                    return_value.append(cut.board)
            elif isinstance(cut, Board):
                return_value.append(cut)
            else:
                raise TypeError("Parameter '{0}, value = '{0}' and type '{1}', should be QuantityBoard or Board.".format(
                    parameter_name, str(cut), type(cut)))

        return return_value

    @staticmethod
    def _sort_large_boards_first(board_list):
        return sorted(board_list, key=lambda board: board.length, reverse=True)

    def _needed_length(self, cut):
        return cut.length + self.saw_blade_width + self.excess_per_cut

    def compute(self):
        """ Computes which cuts should go on which boards.

        :return: List of BoardResult objects.

        Sorts the list of desired cuts and available boards by size, descending order.
        For each cut, places it on the current board if there is enough space.
        If there is not enough space, try the next board.
        """
        # Sort.  Large boards first.
        cuts = self._sort_large_boards_first(self.desired_cuts)
        available = self._sort_large_boards_first(self.available_boards)

        # Start at the first board and the first cut.
        available_index = 0
        cut_index = 0
        length_left = available[available_index].length
        result_boards = []
        result_cuts = []

        # Loop through each desired cut, placing it on a board.
        while cut_index < len(cuts):
            needed_length = self._needed_length(cuts[cut_index])
            if length_left <= needed_length:
                # Move to the next available board.
                result_boards.append(BoardResult(available[available_index], result_cuts))
                result_cuts = []
                available_index += 1
                length_left = available[available_index].length
                continue

            # Append this cut, reduce the length, and move to the next board.
            result_cuts.append(cuts[cut_index])
            length_left -= needed_length
            cut_index += 1

        # Add the current cuts to the list.
        result_boards.append(BoardResult(available[available_index], result_cuts))

        return result_boards


