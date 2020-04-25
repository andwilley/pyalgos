from collections import defaultdict

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # build the tree can use vertex map
        # for each r1, add its children as an item in the dict
        
        # then search the tree for both
        # as we return recursively, return true if you've found one of the regions
        # if we get 2 trues, we've found the nearest common ancestor
        tree = self.build_tree(regions)
        print(tree[1])
        return self.find_first_common_ancestor(tree[0], tree[1], region1, region2)[2]
        
    
    @staticmethod
    def build_tree(region_lists):
        res = defaultdict(list)
        children = set()
        all_regions = set()
        for region_list in region_lists:
            res[region_list[0]] = res[region_list[0]] + region_list[1:]
            children.update(region_list[1:])
            all_regions.update(region_list)
        return (res, (all_regions - children).pop())
    
    def find_first_common_ancestor(self, tree, curr_node, r1, r2):
        r1fnd, r2fnd = r1 == curr_node, r2 == curr_node
        if curr_node not in tree:
            return (r1fnd, r2fnd, curr_node)
        for child in tree[curr_node]:
            print("looking in " + child + "...")
            res = self.find_first_common_ancestor(tree, child, r1, r2)
            r1fnd, r2fnd = r1fnd or res[0], r2fnd or res[1]
            print(curr_node, res[0], res[1], r1fnd, r2fnd)
            if res[0] and res[1]:
                return res
            if r1fnd and r2fnd:
                return (r1fnd, r2fnd, curr_node)
        return (r1fnd, r2fnd, "")
        
