from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import MetaData
from db import Base, engine

graph = create_schema_graph(
    metadata=Base.metadata,
    engine=engine,
    show_datatypes=True,
    show_indexes=True,
    rankdir='LR',
    concentrate=False
)

graph.write_png('er_diagram.png')