from ssm_document_generator.definition.bash_definition import BashDefinition
from ssm_document_generator.definition.metadata.common import access_level, category
from ssm_document_generator.definition.parameters import common

definition = BashDefinition(
    name='dmesg',
    description='Retrieves dmesg content.',
    command_file_name='dmesg.sh',
    metadata=[category('OS'), access_level(1)],
    parameters=[common.regex_filter_expression(), common.entities_limit()]
)
