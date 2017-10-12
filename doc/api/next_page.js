;
define("search-result/modules/positions/main", ["require", "exports", "module", "common/widgets/plat/exposure", "search-result/modules/common/js/config", "common/components/util/emitter", "common/components/pager/main", "common/components/list-base/main", "common/widgets/plat/addIcon"],
function(require) {
    function a(a) {
        if (g(), C($("#footer").hasClass("footer_fix") ? 68 : 0), 1 == a ? j("jids") : j("jids", a), P(), "false" == T) {
            var c = Math.ceil(U.totalCount / U.pageSize);
            $(".totalNum").text(c),
            $(".curNum").text(U.pn)
        } else parseInt(R) > 30 && (R = 30),
        $(".totalNum").text(R),
        $(".curNum").text(E);
        h()
    }
    function c() {
        $(".company_mark").hover(function() {
            $(this).children("span").show()
        },
        function() {
            $(this).children("span").hide()
        })
    }
    function h() {
        function a(a) {
            for (var c = [], h = {},
            i = 0; i < a.length; i++) {
                var g = a[i],
                _ = typeof g + g;
                1 !== h[_] && (c.push(g), h[_] = 1)
            }
            return c
        }
        for (var h = [], i = 0; i < $(".con_list_item").length; i++) h[i] = $(".con_list_item").eq(i).attr("data-companyid");
        h = a(h),
        companyIdStr = h.join(","),
        $.ajax({
            url: GLOBAL_DOMAIN.ctx + "/c/approve.json",
            dataType: "json",
            data: {
                companyIds: companyIdStr
            },
            type: "GET",
            success: function(a) {
                if (1 == a.state) {
                    for (var h = $('<i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>'), g = a.content.data.approveList, _ = [], v = $(".con_list_item"), i = 0; i < v.length; i++) _.push($(v[i]).data("companyid"));
                    for (var i = 0; i < v.length; i++) {
                        var y = $(v[i]).data("companyid");
                        if (1 == g[y]) {
                            var C = $(v[i]).find(".company_name a");
                            C.after(h.clone())
                        }
                    }
                    c()
                }
            },
            error: function() {}
        })
    }
    function g() {
        var a = window.location.toString(),
        c = a.split("#")[1];
        if (c) {
            var t = $("#" + c).offset().top;
            $(window).scrollTop(t)
        }
    }
    function _() {
        $(".add em").each(function() {
            var a = $(this).text().split("·")[0],
            c = "";
            a.length > 5 ? (c = a.substring(0, 5) + "…", $(this).text(c)) : $(this).text().length > 6 && (c = $(this).text().substring(0, 6) + "…", $(this).text(c))
        })
    }
    function v(a, c, h, g, _, $, v) {
        this.key = a,
        this.userId = c,
        this.portrait = h,
        this.realName = g,
        this.positionName = _,
        this.userLevel = $,
        this.canTalk = v
    }
    function y(a, c) {
        var h = a.content.positionResult || {};
        U.data = h.result || [],
        U.curCity = a.content.city || "",
        U.pn = a.content.pageNo || 1,
        U.pageSize = a.content.pageSize || 15,
        U.totalCount = (h.totalCount >= U.maxPage * U.pageSize ? U.maxPage * U.pageSize: h.totalCount) || 0;
        var g = [];
        for (var $ in a.content.hrInfoMap) g.push(new v($, a.content.hrInfoMap[$].userId, a.content.hrInfoMap[$].portrait, a.content.hrInfoMap[$].realName, a.content.hrInfoMap[$].positionName, a.content.hrInfoMap[$].userLevel, a.content.hrInfoMap[$].canTalk));
        for (var y = U.data,
        i = y.length - 1; i >= 0; i--) y[i].curpage = c;
        U.data.hrInfoMap = g || [],
        w(),
        _(),
        U.firstPage && U.totalCount > U.pageSize && (b(), I())
    }
    function C(a) {
        $(window).height() - a > $(document.body).height() ? $("#footer").addClass("footer_fix") : $("#footer").removeClass("footer_fix")
    }
    function w() {
        var a = $("#s_position_list input[name=abtCode]").val().trim(),
        c = new A({
            emitter: O,
            container: G.find(".item_con_list"),
            layout: "#tpl-position-list",
            data: U.data,
            extra: {
                abt: a
            },
            curpage: U.pn,
            curcity: U.curCity,
            noempty: !1,
            nomore: !0,
            layoutempty: "#empty-position"
        });
        c.init()
    }
    function b() {
        var a = new z({
            emitter: O,
            container: G.find(".item_con_pager"),
            totalpage: Math.ceil(U.totalCount / U.pageSize),
            current: U.pn
        });
        a.init()
    }
    function N(a) {
        $("#filterBrief").fadeIn(a),
        $("#filterCollapse").animate({
            opacity: 0,
            height: $("#filterBrief").height
        },
        a,
        function() {
            $("#filterCollapse").hide()
        }),
        $(".btn-collapse").addClass("collapsed"),
        $(".btn-collapse").attr("title", "点击展开筛选项"),
        $("body,html").animate({
            scrollTop: 0
        },
        500)
    }
    function I() {
        function a() {}
        a.prototype = {
            constructor: a,
            init: function() {
                var a = $("#order").find(".page");
                this.elePrev = a.find(".prev"),
                this.eleNext = a.find(".next"),
                this.eleCurNum = a.find(".curNum"),
                this.totalPageNum = Math.ceil(U.totalCount / U.pageSize),
                this.pagerContainer = G.find(".item_con_pager"),
                this.initEvent()
            },
            initEvent: function() {
                var a = this;
                this.elePrev.on("click",
                function() {
                    a.prev()
                }),
                this.eleNext.on("click",
                function() {
                    a.next()
                }),
                this.eventListener()
            },
            setCurNum: function(a) {
                this.eleCurNum.html(a)
            },
            prev: function() {
                this.pagerContainer.find(".pager_prev").trigger("click")
            },
            next: function() {
                this.pagerContainer.find(".pager_next").trigger("click")
            },
            eventListener: function() {
                var a = this;
                O.on("pager:go",
                function(c) {
                    a.setCurNum(c),
                    a.eleCurNum.html() <= 1 ? a.elePrev.addClass("ban") : a.eleCurNum.html() >= a.totalPageNum ? a.eleNext.addClass("ban") : (a.eleNext.removeClass("ban"), a.elePrev.removeClass("ban")),
                    N(500)
                })
            }
        };
        var c = new a;
        c.init()
    }
    function k(a) {
        console.log(a)
    }
    function j(a, c) {
        var h = [],
        g = [],
        _ = [],
        v = $("#s_position_list .con_list_item a.position_link");
        v.each(function(a, c) {
            if ($(c).attr("data-lg-tj-id")) {
                var v = $(c).attr("data-lg-tj-id") || "idnull",
                y = $(c).attr("data-lg-tj-no") || "idnull",
                C = $(c).attr("data-lg-tj-cid") || "idnull",
                w = $(c).attr("data-lg-tj-abt") || "";
                w && "|" != w ? (g.push([v, y, C]), _.push(w)) : h.push([v, y, C])
            }
        }),
        g.length > 0 && _.length > 0 && S(g, "p", _),
        h.length > 0 && S(h, "p");
        var y = encodeURIComponent(document.URL),
        C = $("#s_position_list .con_list_item"),
        w = [];
        C.each(function() {
            var a = $(this).attr("data-positionid");
            w.push(a)
        });
        var b = w.join(","),
        N = Math.random(),
        I = b,
        t = "search",
        k = {
            t: t,
            dl: y,
            z: N
        };
        c && (k.pn = c),
        "jids" == a ? k.jids = I: k.cids = I,
        postoA(k)
    }
    function P() {
        function a(n) {
            switch (n) {
            case 0:
                return 0;
            case 1:
                return 1;
            case 2:
                return 10;
            case 3:
                return 10;
            case 4:
                return 10;
            case 5:
                return 10;
            case 6:
                return 10;
            case 11:
                return 11;
            case 12:
                return 12;
            case 13:
                return 13;
            case 14:
                return 14;
            case 15:
                return 15;
            case 16:
                return 16;
            case 17:
                return 17;
            default:
                return
            }
        }
        function c(a) {
            var c = $("<i class='pos_icon pos_icon_12'></i>");
            a && a.find(".p_top").append(c.clone()),
            $("ul.item_con_list .p_top h3").css("max-width", "180px")
        }
        function h(a, c) {
            if (13 == a && c) {
                var h = $("<i class='pos_icon pos_icon_13'></i>");
                c.find(".company_name").append(h.clone())
            } else if (14 == a && c) {
                var h = $("<i class='pos_icon pos_icon_14'></i>");
                c.find(".company_name").append(h.clone())
            } else if (15 == a && c) {
                var h = $("<i class='pos_icon pos_icon_15'></i>");
                c.find(".company_name").append(h.clone())
            } else if (16 == a && c) {
                var h = $("<i class='pos_icon pos_icon_16'></i>");
                c.find(".company_name").append(h.clone())
            } else if (17 == a && c) {
                var h = $("<i class='pos_icon pos_icon_17'></i>");
                c.find(".company_name").append(h.clone())
            } else if (1 == a && c) {
                var h = $("<i class='pos_icon pos_icon_1'></i>");
                c.find(".company_name").append(h.clone())
            } else if (10 == a && c) {
                var h = $("<i class='pos_icon pos_icon_10'></i>");
                c.find(".company_name").append(h.clone())
            } else if (11 == a && c) {
                var h = $("<i class='pos_icon pos_icon_11'></i>");
                c.find(".company_name").append(h.clone())
            }
            $("ul.item_con_list .p_top h3").css("max-width", "180px")
        }
        function g(a) {
            for (var c = [], h = {},
            i = 0; i < a.length; i++) {
                var g = a[i],
                _ = typeof g + g;
                1 !== h[_] && (c.push(g), h[_] = 1)
            }
            return c
        }
        for (var _ = [], v = $(".con_list_item"), i = 0; i < v.length; i++) _.push($(v[i]).data("companyid"));
        _ = g(_);
        var y = _.join(","),
        C = require("common/widgets/plat/addIcon").loadIconInfo;
        C({
            type: "COMPANY",
            ids: y
        }).done(function(g) {
            if (g && "" != g) for (var i = 0; i < v.length; i++) {
                var _ = v.eq(i).data("companyid");
                12 == a(g[_]) ? c(v.eq(i)) : 13 == a(g[_]) ? h(g[_], v.eq(i)) : 14 == a(g[_]) ? h(g[_], v.eq(i)) : 15 == a(g[_]) ? h(g[_], v.eq(i)) : 16 == a(g[_]) ? h(g[_], v.eq(i)) : 17 == a(g[_]) ? h(g[_], v.eq(i)) : 1 == a(g[_]) ? h(g[_], v.eq(i)) : 10 == a(g[_]) ? h(g[_], v.eq(i)) : 11 == a(g[_]) && h(g[_], v.eq(i))
            }
        }).fail(function() {})
    }
    var S = require("common/widgets/plat/exposure").exposure;
    postoA = require("common/widgets/plat/exposure").postoA;
    var M = require("search-result/modules/common/js/config"),
    L = require("common/components/util/emitter"),
    O = new L,
    z = require("common/components/pager/main"),
    A = require("common/components/list-base/main"),
    T = $("#isSEO").val(),
    E = $("#pageNoSEO").val(),
    R = $("#totalPageCountSEO").val(),
    B = $("#resultLengthSEO").val(),
    D = $("#filterOption").val(),
    G = $("#s_position_list"),
    U = {
        firstPage: !0,
        maxPage: 30
    };
    $(".add em").each(function() {
        var a = $(this).text().split("·")[0],
        c = "";
        a.length > 5 ? (c = a.substring(0, 5) + "…", $(this).text(c)) : $(this).text().length > 6 && (c = $(this).text().substring(0, 6) + "…", $(this).text(c))
    }),
    global.needAddtionalResult && ($(".no_position_wrapper .curr_com").text(global.keyword.length > 6 ? global.keyword.substring(0, 6) + "...": global.keyword), $(".no_position_wrapper .curr_city").text(global.queryParam.city));
    var Y = {
        getList: function(c) {
            global.keyword;
            $.ajax({
                url: M.url.positonlist + "?" + global.queryParamStr,
                dataType: "json",
                data: c,
                type: "POST",
                success: function(h) {
                    0 == h.content.positionResult.length && global.needAddtionalResult && $(".no_position_wrapper").hide(),
                    y(h, c.pn),
                    a(c.pn)
                },
                error: function(a) {
                    k(a)
                }
            })
        }
    },
    F = {
        first: !0,
        pn: 1,
        kd: global.keyword
    };
    "false" == T ? Y.getList(F) : (1 != E && (F.first = !1, U.firstPage = !1), F.pn = parseInt(E), F.kd = global.keyword, 0 == B && global.needAddtionalResult && $(".no_position_wrapper").hide(), _(), a(parseInt(E)), "2" == D && N(500)),
    O.on("pager:go",
    function(a) {
        F.first = !1,
        F.pn = a,
        F.kd = global.keyword,
        U.pn = a,
        U.firstPage = !1,
        Y.getList(F)
    }),
    $(".pager_container a, #order .page a").on("click",
    function(e) {
        e.preventDefault(),
        "1" == D || $("#filterCollapse").hasClass("collapsed") ? window.location.href = $(this).attr("href") + "?filterOption=2": ("2" == D || "3" == D) && (window.location.href = $(this).attr("href") + "?filterOption=3")
    }),
    $(".pager_container .page_no, #order .page .curNum").on("click",
    function() {
        var a = $(this);
        a.hasClass("pager_prev_disabled") || a.hasClass("pager_is_current") || a.hasClass("pager_next_disabled") || $("body,html").animate({
            scrollTop: 0
        },
        500)
    })
});