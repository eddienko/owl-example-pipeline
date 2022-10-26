from pathlib import Path

import voluptuous as vo

schema = vo.Schema(
    {
        vo.Required("datalen"): vo.Range(1, 1000),  
        vo.Optional("input_path"): vo.Coerce(Path), 
        vo.Optional("output_path"): vo.Coerce(Path),
    }
)
"""
Example pipeline configuration schema.

Parameters
----------

datalen : int
    Length of data, between 1 and 1000.
output : str
    Output directory.
"""
