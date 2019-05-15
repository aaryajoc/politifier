


"""
Some sample request documents, pre-processed 
and ready for politeness classification.

Shows expected format of documents--
Each document is a dict with fields
'text', 'sentences', and 'parses'

the 'score' field is only required
when training models. 
A score > 0.0 means the request is polite.

"""

TEST_DOCUMENTS = [
    # Polite requests
    # Req 1
    {
        "text": "Have you found the answer for your question? If yes would you please share it?", 
        "sentences": [
            "Have you found the answer for your question?", 
            "If yes would you please share it?"
        ],
        "parses": [
            ["csubj(found, Have)", "dobj(Have, you)", "root(ROOT, found)", "det(answer, the)", "dobj(found, answer)", "poss(question, your)", "prep_for(found, question)"], 
            ["prep_if(would, yes)", "root(ROOT, would)", "nsubj(would, you)", "ccomp(would, please)", "nsubj(it, share)", "xcomp(please, it)"]
        ],
    }, 
    # # Req 2
    # {
    #     "text": "Sorry :) I dont want to hack the system!! :) is there another way?", 
    #     "sentences": [
    #         "Sorry :) I dont want to hack the system!!", 
    #         ":) is there another way?"
    #     ],
    #     "parses": [
    #         ["nsubj(dont-5, I-4)", "xsubj(hack-8, I-4)", "rcmod(-RRB--3, dont-5)", "dep(dont-5, want-6)", "aux(hack-8, to-7)", "xcomp(want-6, hack-8)", "det(!!-11, the-9)", "nn(!!-11, system-10)", "dobj(hack-8, !!-11)"], 
    #         ["cop(there-4, is-3)", "root(ROOT-0, there-4)", "det(way-6, another-5)", "dep(there-4, way-6)"]
    #     ],
    # },
    # # Impolite requests
    # # Req 3
    # {
    #     "text": "What are you trying to do?  Why can't you just store the \"Range\"?",
    #     "sentences": [
    #         "What are you trying to do?",
    #         "Why can't you just store the 'Range'?"
    #     ],
    #     "parses": [
    #         ["dep(trying-4, What-1)", "aux(trying-4, are-2)", "nsubj(trying-4, you-3)", "xsubj(do-6, you-3)", "root(ROOT-0, trying-4)", "aux(do-6, to-5)", "xcomp(trying-4, do-6)"],
    #         ["advmod(ca-2, Why-1)", "advcl(store-6, ca-2)", "neg(ca-2, n't-3)", "nsubj(store-6, you-4)", "advmod(store-6, just-5)", "root(ROOT-0, store-6)", "det(Range-9, the-7)", "dobj(store-6, Range-9)"]
    #     ],
    # },
    # # Req 4
    # {
    #     "text": "This was supposed to have been moved to &lt;url&gt; per the cfd. why wasn't it moved?",
    #     "sentences": [
    #         "this was supposed to have been moved to &lt;url&gt; per the cfd.",
    #         "why wasn't it moved?"
    #     ],
    #     "parses": [
    #         ["nsubjpass(supposed-3, this-1)", "xsubj(moved-7, this-1)", "auxpass(supposed-3, was-2)", "root(ROOT-0, supposed-3)", "aux(moved-7, to-4)", "aux(moved-7, have-5)", "auxpass(moved-7, been-6)", "xcomp(supposed-3, moved-7)", "prep_to(moved-7, url-10)", "det(cfd-14, the-13)", "prep_per(url-10, cfd-14)"],
    #         ["advmod(n't-3, why-1)", "cop(n't-3, was-2)", "root(ROOT-0, n't-3)", "nsubj(moved-5, it-4)", "dep(n't-3, moved-5)"]
    #     ],
    # }
]







