class Parent:
    class_protected = "_parent_class_var" #protected attr  ( - )
    __class_private = "__parent_class_private" #private attr ( __ )
    
    def __init__(self, name):
        self._protected_attr = f"protected_{name}"
        self.__private_attr = f"private_{name}"
    
    def _protected_method(self):
        return f"Parent protected: {self._protected_attr}"
    
    def __private_method(self):
        return f"Parent private: {self.__private_attr}"
    
    def public_access(self):
        return self.__private_method()

class Child(Parent):
    class_protected = "_child_class_var"
    __class_private = "__child_class_private"
    
    def __init__(self, name, age):
        super().__init__(name)
        self._child_protected = f"child_{age}"
        self.__child_private = f"child_private_{age}"
    
    def _protected_method(self):
        parent_result = super()._protected_method()
        return f"{parent_result} | Child protected: {self._child_protected}"
    
    def __child_private_method(self):
        return f"Child private method: {self.__child_private}"
    
    def access_all(self):
        # Can access parent's protected via super()
        protected = super()._protected_method()
        # Cannot directly access parent's private method via super()
        public = super().public_access()
        # Own private method
        child_private = self.__child_private_method()
        
        return {
            'protected_via_super': protected,
            'parent_private_via_public': public,
            'child_private': child_private,
            'class_protected': self.class_protected,
            'parent_class_protected': Parent.class_protected
        }

# Demonstration
child = Child("Alice", 25)
result = child.access_all()

print("=== Inheritance with super() Demo ===")
for key, value in result.items():
    print(f"{key}: {value}")

print(f"\nDirect protected access: {child._protected_method()}")
print(f"Protected attribute: {child._protected_attr}")

# Show name mangling for private attributes
print(f"\nName mangling demo:")
print(f"Child private attr (mangled): {child._Child__child_private}")
print(f"Parent private attr (mangled): {child._Parent__private_attr}")
