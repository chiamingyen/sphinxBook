# -*- coding: utf-8 -*-
class Directive(object):
    """
    Fake Directive class to allow Sphinx directives to be written in
    class style.
    """
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = None
    has_content = False
    ###1###
    def __init__(self, name, arguments, options, content, lineno,
                 content_offset, block_text, state, state_machine):
        self.name = name
        self.arguments = arguments  #{1}
        self.options = options      #{2}
        self.content = content
        self.lineno = lineno        #{3}
        self.content_offset = content_offset
        self.block_text = block_text
        self.state = state
        self.state_machine = state_machine
    ###1###
    ###2###
    def run(self):
        raise NotImplementedError('Must override run() is subclass.')
    ###2###