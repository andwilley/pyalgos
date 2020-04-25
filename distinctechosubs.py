class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        all_subs = set([])
        dub_subs = set([])

        for c in text:
            temp_subs = set([])

            for sub in all_subs:
                new_sub = sub + c
                temp_subs.add(sub + c)
                if len(new_sub) >= 2 and len(new_sub) % 2 == 0 and new_sub[:len(new_sub) // 2] == new_sub[len(new_sub) // 2:]:
                    dub_subs.add(new_sub)

            temp_subs.add(c)
            all_subs = temp_subs

        return len(dub_subs)