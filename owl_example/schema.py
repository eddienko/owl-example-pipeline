import voluptuous as vo

schema = vo.Schema(
    {vo.Required("datalen"): vo.Range(1, 1000)}
)
"""
Example pipeline configuration schema.

Parameters
----------

datalen : int
    Length of data, between 1 and 1000
"""
