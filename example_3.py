#! /usr/bin/python3.6

"""

    Example 3:

    Find all points in the CATPart and print to console -> and export to csv.

"""

import csv

from pycatia import catia
from pycatia.space_analyses_interfaces.spa_workbench import SPAWorkbench

documents = catia.documents
documents.open(r'tests\CF_catia_measurable_part.CATPart')

document = catia.active_document

spa_workbench = SPAWorkbench(document.document)
part = document.part()

selected = document.search_for_items(document, ['Point'])

# export the points to a csv file.
csv_file_name = '__junk__\\exported_points.csv'
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    for selection in selected:
        reference = part.create_reference_from_object(selection)
        measurable = spa_workbench.get_measurable(reference)

        # print to console.
        print(selection.name, measurable.get_point())

        x, y, z = measurable.get_point()
        csv_writer.writerow([selection.name, x, y, z])
