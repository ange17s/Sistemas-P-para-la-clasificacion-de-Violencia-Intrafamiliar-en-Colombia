import constants

class Membrane:
    def __init__(self, parent_membrane, label):
        self.ident = next(constants.next_membrane_ident)
        self.inner_membranes = set()
        self.parent_membrane = parent_membrane
        if parent_membrane:
            parent_membrane.inner_membranes.add(self)
        self.objects = dict()
        self.label = label
        self.blocked = False

    def add_object(self, obj, count=1):
        if obj in self.objects:
            self.objects[obj] += count
        else:
            self.objects[obj] = count

    def __str__(self, level=0, deepness=constants.MAX_INT):
        if self.label == '#' and len(self.objects) == 0:
            return ''
        ret = ' ' * level
        ret += '{}: {}\n'.format(self.label, ', '.join(f"{k}^{v}" for k, v in self.objects.items()))
        if deepness > 0:
            for membrane in self.inner_membranes:
                ret += membrane.__str__(level + 1, deepness - 1)
        return ret

    def get_classification(self, reglas_membranas):
        for regla in reglas_membranas:
            condiciones = regla.split(" -> ")[0].strip("[] ").replace("Si ", "").split("AND")
            clase = regla.split(" -> ")[1].strip("[] ").strip()

            if all(self.objects.get(cond.strip(), float('inf')) > 0 for cond in condiciones):
                return clase
        return None
