
from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship
from database import Base

class Inscripcion(Base):
    __tablename__ = "inscripciones"

    id = Column(Integer, primary_key=True, index=True)
    nombre_estudiante = Column(String(100), nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)

    curso = relationship("Curso", back_populates="inscription")