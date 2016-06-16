# Demo on how to stop a graph execution

from datamodel.base import graph, exceptions
from datamodel.nodes import value, apply


def execution_stop(number):

    def stop_here(value):
        if value >= 0:
            raise exceptions.StopGraphExecutionSignal('arg is positive')
        raise exceptions.StopGraphExecutionSignal('arg is negative')

    v = value.Value(number)
    a = apply.ApplyStatic(stop_here)

    g = graph.Graph('execution_stop', [a, v])

    g.connect(a, v)

    return g