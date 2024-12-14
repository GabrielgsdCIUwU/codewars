def same_structure_as(original, other):
    def check_structure(orign, oth):
        
        if isinstance(orign, list) and isinstance(oth, list):
            if len(orign) != len(oth):
                return False
            
            for i in range(len(orign)):
                if not check_structure(orign[i], oth[i]):
                    return False
        
        elif isinstance(orign, list) or isinstance(oth, list):
            return False
        
        return True

    return check_structure(original, other)