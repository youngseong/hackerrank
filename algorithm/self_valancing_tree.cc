// https://www.hackerrank.com/challenges/self-balancing-tree/problem

/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */


node * insert(node * root,int val)
{
	std::vector<node*> trace;
    node *prev = nullptr, *curr = root;
    
    node* inserted = new node();
    inserted->val = val;
    inserted->ht = 0;
    inserted->left = inserted->right = nullptr;
    
    while (curr->val != val)
    {
        trace.push_back(curr);
        prev = curr;
        
        if (val < curr->val)
        {
            if (curr->left == nullptr)
                curr->left = inserted;
            curr = curr->left;
        }
        else
        {
            if (curr->right == nullptr)
                curr->right = inserted;
            curr = curr->right;
        }
    }
    trace.push_back(curr);
    
    vector<int> balFacts(trace.size());
    
    auto updateHeight_ = [](node* n)
    {
        int hl = n->left ? n->left->ht : -1;
        int hr = n->right ? n->right->ht : -1;
        
        n->ht = std::max(hl, hr) + 1;
    };
    
    for (int i = trace.size() - 1; i >= 0; --i)
    {
        auto n = trace[i];
        int hl = n->left ? n->left->ht : -1;
        int hr = n->right ? n->right->ht : -1;
        
        balFacts[i] = hl - hr;
        
        updateHeight_(n);
    }
    
    for (int i = trace.size() - 2; i >= 0; --i)
    {
        bool processed = true;
        node *r = nullptr;
        
        switch (balFacts[i])
        {
            case 2:
                if (balFacts[i+1] == 1) // LL
                {
                    r = trace[i+1];
                    trace[i]->left = r->right;
                    r->right = trace[i];
                }
                else // LR
                {
                    r = trace[i+2];
                    trace[i+1]->right = r->left;
                    trace[i]->left = r->right;
                    r->left = trace[i+1];
                    r->right = trace[i];
                }
                break;
            case -2:
                if (balFacts[i+1] == -1) // RR
                {
                    r = trace[i+1];
                    trace[i]->right = r->left;
                    r->left = trace[i];
                }
                else // RL
                {
                    r = trace[i+2];
                    trace[i+1]->left = r->right;
                    trace[i]->right = r->left;
                    r->right = trace[i+1];
                    r->left = trace[i];
                }
                break;
            default:
                processed = false;
        }
        
        if (processed)
        {
            updateHeight_(r->left);
            updateHeight_(r->right);
            updateHeight_(r);

            if (i > 0)
            {
                if (trace[i-1]->val < r->val)
                    trace[i-1]->right = r;
                else
                    trace[i-1]->left = r;
                
                for (int j = i-1; j >= 0; --j)
                    updateHeight_(trace[j]);
            }
            else
            {
                root = r;
            }
            
            break;
        }
    }
    
    return root;
}
