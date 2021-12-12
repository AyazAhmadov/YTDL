from dataclasses import dataclass

@dataclass
class IrrelevantArgumentError(Exception):
    main_var: str
    aux_var: str
    val: str
    message: str='\'{}\' argument cannot be set if \'{}\' is set to \'{}\''

    def __str__(self) -> str:
        return self.message.format(self.aux_var, self.main_var, self.val)