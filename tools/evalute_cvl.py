#!/usr/bin/python

mport sys
import wi19

params = {
    "gt_csv": "./test_data/gt.csv",
    "submission_csv": "./test_data/dm.json",
    "roc_path": "",
    "html_path":""
}

params, help_str = wi19.get_arg_switches(params)

wi19.print_single_submission_table(
    params["submission_csv"],
    params["gt_csv"],
    roc_svg_path=params["roc_path"])
