from ScriptingLanguage.Tokens import EOF

__author__ = 'chronium'

class Matcher(object):
    def is_match(self, tokenizer):
        pass

class MatcherBase(Matcher):
    def is_match(self, tokenizer):
        if tokenizer.end():
            return EOF()

        tokenizer.take_snapshot()
        match = self.is_match_impl(tokenizer)

        if match:
            tokenizer.commit_snapshot()
        else:
            tokenizer.rollback_snapshot()

        return match

    def is_match_impl(self, tokenizer):
        return None
