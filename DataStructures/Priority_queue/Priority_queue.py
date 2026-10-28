from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import pq_entry as pqe


def default_compare_higher_value(father_node, child_node):
    """True si el nodo padre tiene MAYOR prioridad (valor mayor) que el hijo."""
    return pqe.get_priority(father_node) > pqe.get_priority(child_node)


def default_compare_lower_value(father_node, child_node):
    """True si el nodo padre tiene MENOR prioridad (valor menor) que el hijo."""
    return pqe.get_priority(father_node) < pqe.get_priority(child_node)


def new_heap(is_min_pq=True):
    """Crea una cola de prioridad indexada orientada a menor (por defecto) o mayor."""
    if is_min_pq:
        cmp_function = default_compare_lower_value
    else:
        cmp_function = default_compare_higher_value

    return {
        "elements": lt.new_list(),
        "size": 0,
        "cmp_function": cmp_function,
    }


def priority(my_heap, parent, child):
    """
    Usa la función de comparación del heap sobre dos entradas.
    True si 'parent' debe estar por encima de 'child' en el heap.
    """
    return my_heap["cmp_function"](parent, child)


def exchange(my_heap, pos1, pos2):
    """Intercambia las entradas de las posiciones pos1 y pos2 (base 1)."""
    elements = my_heap["elements"]
    entry1 = lt.get_element(elements, pos1 - 1)
    entry2 = lt.get_element(elements, pos2 - 1)
    lt.change_info(elements, pos1 - 1, entry2)
    lt.change_info(elements, pos2 - 1, entry1)
    return my_heap


def size(my_heap):
    """Número de elementos en la cola de prioridad."""
    return my_heap["size"]


def is_empty(my_heap):
    """True si la cola de prioridad no tiene elementos."""
    return size(my_heap) == 0


def swim(my_heap, pos):
    """Sube el elemento en 'pos' (base 1) hasta restaurar el orden del heap."""
    elements = my_heap["elements"]
    while pos > 1:
        parent_pos = pos // 2
        parent = lt.get_element(elements, parent_pos - 1)
        child = lt.get_element(elements, pos - 1)
        # Sube solo si el hijo tiene estrictamente más prioridad que el padre
        if priority(my_heap, child, parent):
            exchange(my_heap, parent_pos, pos)
            pos = parent_pos
        else:
            break
    return my_heap


def insert(my_heap, priority_value, value):
    """Inserta una nueva entrada (priority_value, value) y reordena con swim."""
    entry = pqe.new_pq_entry(priority_value, value)
    lt.add_last(my_heap["elements"], entry)
    my_heap["size"] += 1
    swim(my_heap, my_heap["size"])
    return my_heap