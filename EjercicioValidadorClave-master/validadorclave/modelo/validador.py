from abc import ABC, abstractmethod
from modelo.errores import (LongitudInvalidaError,
  SinMayusculaError,
  SinMinusculaError,
  SinNumeroError,
  SinCaracterEspecialError,
  SinCalistoError
)

class ReglaValidacion(ABC):

  def __init__(self, longitud_esperada):
    self.longitud_esperada = longitud_esperada

  @abstractmethod
  def es_valida(self, clave):
    pass
  
  def _validar_longitud(self, clave):
    if len(clave) <= self.longitud_esperada:
      raise LongitudInvalidaError("La longitud de la clave no cumple con lo esperado.")
    
  def _contiene_mayuscula(self, clave):
    for c in clave:
      if c.isupper():
        return True
    raise SinMayusculaError("La clave debe contener al menos una letra mayúscula.")

  def _contiene_minuscula(self, clave):
    for c in clave:
      if c.islower():
        return True
    raise SinMinusculaError("La clave debe contener al menos una letra minuscula.")
  
  def _contiene_numero(self, clave):
    for c in clave:
      if c.isdigit():
        return True
    raise SinNumeroError("La clave debe contener al menos una número.")

class ReglaValidacionGanimedes(ReglaValidacion):
  
  def __init__(self):
    super().__init__(8)

  def contiene_caracter_especial(self, clave):
    caracteres_especiales = '@_#$%'
    for c in clave:
      if c in caracteres_especiales:
        return True
    raise SinCaracterEspecialError("La clave debe contener al menos un carácter especial: @, _, #, $ o %.")

  def es_valida(self, clave):
    try:
      self._validar_longitud(clave)
      self._contiene_mayuscula(clave)
      self._contiene_minuscula(clave)
      self._contiene_numero(clave)
      self.contiene_caracter_especial(clave)
    except Exception as e:
      raise e
    else:
      return True

class ReglaValidacionCalisto(ReglaValidacion):
  
  def __init__(self):
    super().__init__(6)

  def contiene_calisto(self, clave):
    if clave.find('cAliStO') != -1:
      return True
    raise SinCalistoError("La clave debe contener la palabra 'calisto' escrita con al menos dos letras mayúsculas, pero no todas.")

  def es_valida(self, clave):
    try:
      self._validar_longitud(clave)
      self._contiene_numero(clave)  
      self.contiene_calisto(clave)
    except Exception as e:
      raise e
    else:
      return True

class Validador:

  def __init__(self, regla):
    self.regla = regla

  def es_valida(self, clave):
    return self.regla.es_valida(clave)