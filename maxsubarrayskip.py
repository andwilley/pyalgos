def maximumSum(self, arr: List[int]) -> int:

    max_no_skip = arr[0]
    max_end_here = [arr[0]] * len(arr)
    for i in range(1, len(arr)):
        max_end_here[i] = max(max_end_here[i - 1] + arr[i], arr[i])
        max_no_skip = max(max_no_skip, max_end_here[i])
    max_start_here = [arr[-1]] * len(arr)
    for i in range(len(arr) - 2, -1, -1):
        max_start_here[i] = max(max_start_here[i + 1] + arr[i], arr[i])
    max_with_skip = max_no_skip
    for i in range(1, len(arr) - 1):
        max_with_skip = max(max_with_skip, max_end_here[i - 1] + max_start_here[i + 1])
    return max_with_skip

# FFFFHFFFFGGGFGFGFG
#         FGFFG
# RRSRSRTSRR
#      RRRRS