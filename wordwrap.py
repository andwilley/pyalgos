class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # edge: a word is longer than cols

        # for each word, if there is room from current index to end of line, add it
        # add a space (if at end of line or space gets to end of line -> new line)

        if not sentence:
            return ''

        line_num = 1
        reps = 0
        line_index = 0
        word_index = 0
        overflow = False


        """
        I Had Apple Pie
        4 rows, 5 columns

        I had
        apple
        pie I
        (1)

        cols = 6
        word-- : set line index to line_index + len(word)  + 1
        wordd- : set line index to 0
        worddd : set line index to 0
        wordddd: set line index to len(word)

        li = 5
        wi = 6
        ln = 4
        reps = 1
        word = apple
        of = False
        """

        while line_num <= rows:
            word = sentence[word_index % len(sentence)]
            if len(word) > cols:
                return -1
            # if it fits, add it, change line_index and word_index, if not, reset the line index
            if line_index + len(word) < cols - 1:
                line_index = line_index + len(word) + 1
            elif line_index + len(word) > cols:
                word_index -= 1
                line_index = 0
                line_num += 1
            else:
                line_index = 0
                line_num += 1
            # incr word_index
            word_index += 1
            # new line num may exceed available rows here
            if word_index % len(sentence) == 0:
                reps += 1
        return reps