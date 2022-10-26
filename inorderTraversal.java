class Solution {
    List<Integer > ans = new LinkedList<>();
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root == null)
            return ans;
        inorderTraversal(root.left);
        ans.add(root.val);
        inorderTraversal(root.right);
        return ans;
        
    }
}
