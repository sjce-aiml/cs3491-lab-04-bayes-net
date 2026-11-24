"""Lab 4 starter code: Bayesian network inference by enumeration."""

def probability(bn, var, value, assignment):
    raise NotImplementedError('TODO: implement this')

def topological_order(bn):
    raise NotImplementedError('TODO: implement this')

def enumerate_all(bn, variables, assignment):
    raise NotImplementedError('TODO: implement this')

def enumeration_ask(query, evidence, bn):
    """Return {True: p, False: p} for P(query | evidence)."""
    raise NotImplementedError('TODO: implement this')

def learn_cpts(data, structure):
    """Learn a Bayesian network from data.
data: list of dicts {var: bool}; structure: {var: [parents]}.
Return bn in the same format used by enumeration_ask: {var: (parents, {parent_values: P(var=True)})}.
Uses Laplace (add-one) smoothing."""
    raise NotImplementedError('TODO: implement this')

def draw_network(bn, path='bayes_net.png'):
    """Draw the conditional dependencies (parent -> child arrows) and save to `path`.
Return the list of edges drawn."""
    raise NotImplementedError('TODO: implement this')
