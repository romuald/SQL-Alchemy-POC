Here is the full traceback::

	Traceback (most recent call last):
	  File "example.py", line 9, in <module>
		print session.query(SecondDomain).one()
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/orm/session.py", line 839, in query
		return self._query_cls(entities, self, **kwargs)
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/orm/query.py", line 105, in __init__
		self._set_entities(entities)
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/orm/query.py", line 114, in _set_entities
		self._setup_aliasizers(self._entities)
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/orm/query.py", line 129, in _setup_aliasizers
		_entity_info(entity)
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/orm/util.py", line 554, in _entity_info
		mapper = mapper.compile()
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/orm/mapper.py", line 797, in compile
		mapper._post_configure_properties()
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/orm/mapper.py", line 827, in _post_configure_properties
		prop.init()
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/orm/interfaces.py", line 494, in init
		self.do_init()
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/orm/properties.py", line 893, in do_init
		self._process_dependent_arguments()
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/orm/properties.py", line 937, in _process_dependent_arguments
		setattr(self, attr, getattr(self, attr)())
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/ext/declarative.py", line 1187, in return_cls
		x = eval(arg, globals(), d)
	  File "<string>", line 1, in <module>
	  File "/usr/lib/python2.7/dist-packages/sqlalchemy/ext/declarative.py", line 1163, in __getattr__
		% (self.cls, key))
	sqlalchemy.exc.InvalidRequestError: Class <class 'second.Domain_'> does not have a mapped column named 'owner_id'
