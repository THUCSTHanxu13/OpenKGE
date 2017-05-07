/**
 * Created by Limteng on 11/16/14.
 */
$(document).ready(function() {
    // initialize the plugin, pass in the class selector for the sections of content (blocks)
    // var scrollorama = $.scrollorama({ blocks:'.scrollblock' });

    // scrollorama
    //     .animate("#func-title", {delay: 150, duration: 200, property:'opacity', start: 0})
    //     .animate("#soa-title", {delay: 150, duration: 200, property:'opacity', start: 0})
    //     .animate("#smt-title", {delay: 150, duration: 200, property:'opacity', start: 0})
    //     .animate("#team-title", {delay: 150, duration: 200, property:'opacity', start: 0});

    // scrollorama
    //     .animate('#kwtitle', {duration: 200, property:'top', end: 0})
    //     .animate('#kwlab', {duration: 500, property:'top', end: 0})
    //     .animate('#kwarrow', {duration: 800, property:'top', end: 0});

    // scrollorama
    //     .animate("#func-img1", { delay: 0, duration:500, property:"rotate", start: 360})
    //     .animate("#func-img1", { delay: 400, duration:100, property:"opacity", start: 0})
    //     .animate("#func-img2", { delay: 50, duration:500, property:"rotate", start: 360})
    //     .animate("#func-img2", { delay: 450, duration:100, property:"opacity", start: 0})
    //     .animate("#func-img3", { delay: 100, duration:500, property:"rotate", start: 360})
    //     .animate("#func-img3", { delay: 500, duration:100, property:"opacity", start: 0});

    // scrollorama
    //     .animate("#funcblock1 > .functitle", { delay: 450, duration: 80, property:'left', start:-10})
    //     .animate("#funcblock1 > .functitle", { delay: 450, duration: 80, property:'opacity', start:0})
    //     .animate("#funcblock2 > .functitle", { delay: 500, duration: 80, property:'left', start:-10})
    //     .animate("#funcblock2 > .functitle", { delay: 500, duration: 80, property:'opacity', start:0})
    //     .animate("#funcblock3 > .functitle", { delay: 550, duration: 80, property:'left', start:-10})
    //     .animate("#funcblock3 > .functitle", { delay: 550, duration: 80, property:'opacity', start:0});

    // scrollorama
    //     .animate("#funcblock1 > .funcintro", { delay: 500, duration: 80, property:'left', start:-10})
    //     .animate("#funcblock1 > .funcintro", { delay: 500, duration: 80, property:'opacity', start:0})
    //     .animate("#funcblock2 > .funcintro", { delay: 550, duration: 80, property:'left', start:-10})
    //     .animate("#funcblock2 > .funcintro", { delay: 550, duration: 80, property:'opacity', start:0})
    //     .animate("#funcblock3 > .funcintro", { delay: 600, duration: 80, property:'left', start:-10})
    //     .animate("#funcblock3 > .funcintro", { delay: 600, duration: 80, property:'opacity', start:0});

    // scrollorama
    //     .animate("#soa-img1", { delay: 350, duration:100, property:'top', start:-50})
    //     .animate("#soa-img1", { delay: 350, duration:100, property:'opacity', start:0})
    //     .animate("#soa-img2", { delay: 400, duration:100, property:'top', start:-50})
    //     .animate("#soa-img2", { delay: 400, duration:100, property:'opacity', start:0})
    //     .animate("#soa-img3", { delay: 450, duration:100, property:'top', start:-50})
    //     .animate("#soa-img3", { delay: 450, duration:100, property:'opacity', start:0})
    //     .animate("#soa-img4", { delay: 500, duration:100, property:'top', start:-50})
    //     .animate("#soa-img4", { delay: 500, duration:100, property:'opacity', start:0});
    
    // scrollorama
    //     .animate("#soa-subtitle1", { delay: 400, duration: 80, property:'left', start:-10})
    //     .animate("#soa-subtitle1", { delay: 400, duration: 80, property:'opacity', start:0})
    //     .animate("#soa-subtitle2", { delay: 450, duration: 80, property:'left', start:-10})
    //     .animate("#soa-subtitle2", { delay: 450, duration: 80, property:'opacity', start:0})
    //     .animate("#soa-subtitle3", { delay: 500, duration: 80, property:'left', start:-10})
    //     .animate("#soa-subtitle3", { delay: 500, duration: 80, property:'opacity', start:0})
    //     .animate("#soa-subtitle4", { delay: 550, duration: 80, property:'left', start:-10})
    //     .animate("#soa-subtitle4", { delay: 550, duration: 80, property:'opacity', start:0});

    // scrollorama
    //     .animate("#soa-intro1", { delay: 450, duration: 80, property:'left', start:-10})
    //     .animate("#soa-intro1", { delay: 450, duration: 80, property:'opacity', start:0})
    //     .animate("#soa-intro2", { delay: 500, duration: 80, property:'left', start:-10})
    //     .animate("#soa-intro2", { delay: 500, duration: 80, property:'opacity', start:0})
    //     .animate("#soa-intro3", { delay: 550, duration: 80, property:'left', start:-10})
    //     .animate("#soa-intro3", { delay: 550, duration: 80, property:'opacity', start:0})
    //     .animate("#soa-intro4", { delay: 600, duration: 80, property:'left', start:-10})
    //     .animate("#soa-intro4", { delay: 600, duration: 80, property:'opacity', start:0});

    // scrollorama
    //     .animate('#smt-overall', {delay: 250, duration: 80, property: 'opacity', start: 0});

    // scrollorama
    //     .animate("#smt-block1 > img", { delay: 300, duration: 80, property:'opacity', start:0})
    //     .animate("#smt-block1 > img", { delay: 300, duration: 80, property:'top', start:-20})
    //     .animate("#smt-block2 > img", { delay: 400, duration: 80, property:'opacity', start:0})
    //     .animate("#smt-block2 > img", { delay: 400, duration: 80, property:'top', start:-20})
    //     .animate("#smt-block3 > img", { delay: 500, duration: 80, property:'opacity', start:0})
    //     .animate("#smt-block3 > img", { delay: 500, duration: 80, property:'top', start:-20})
    //     .animate('.smt-arrow', { delay: 630, duration: 50, property:'opacity', start:0});

    // scrollorama
    //     .animate("#smt-block1 > .smt-subtitle", { delay: 350, duration: 80, property:'opacity', start:0})
    //     .animate("#smt-block1 > .smt-subtitle", { delay: 350, duration: 80, property:'left', start:-20})
    //     .animate("#smt-block2 > .smt-subtitle", { delay: 450, duration: 80, property:'opacity', start:0})
    //     .animate("#smt-block2 > .smt-subtitle", { delay: 450, duration: 80, property:'left', start:-20})
    //     .animate("#smt-block3 > .smt-subtitle", { delay: 550, duration: 80, property:'opacity', start:0})
    //     .animate("#smt-block3 > .smt-subtitle", { delay: 550, duration: 80, property:'left', start:-20});

    // scrollorama
    //     .animate("#smt-block1 > .smt-intro", { delay: 380, duration: 80, property:'opacity', start:0})
    //     .animate("#smt-block1 > .smt-intro", { delay: 380, duration: 80, property:'left', start:-30})
    //     .animate("#smt-block2 > .smt-intro", { delay: 480, duration: 80, property:'opacity', start:0})
    //     .animate("#smt-block2 > .smt-intro", { delay: 480, duration: 80, property:'left', start:-30})
    //     .animate("#smt-block3 > .smt-intro", { delay: 580, duration: 80, property:'opacity', start:0})
    //     .animate("#smt-block3 > .smt-intro", { delay: 580, duration: 80, property:'left', start:-30});

    
    // scrollorama
    //     .animate('#team-member-1', { delay: 510, duration: 50, property:'opacity', start:0})
    //     .animate('#team-member-3', { delay: 450, duration: 50, property:'opacity', start:0})
    //     .animate('#team-member-6', { delay: 620, duration: 50, property:'opacity', start:0})
    //     .animate('#team-member-7', { delay: 570, duration: 50, property:'opacity', start:0})
    //     .animate('#team-member-4', { delay: 540, duration: 50, property:'opacity', start:0})
    //     .animate('#team-member-5', { delay: 510, duration: 50, property:'opacity', start:0})
    //     .animate('#team-member-2', { delay: 480, duration: 50, property:'opacity', start:0})
    //     .animate('#team-member-8', { delay: 600, duration: 50, property:'opacity', start:0})
    //     .animate('#team-member-9', { delay: 580, duration: 50, property:'opacity', start:0})
    //     .animate('#team-member-10', { delay: 650, duration: 50, property:'opacity', start:0});

    // scrollorama
    //     .animate('#team-background', { delay: 1000, duration: 300, property:'opacity', start:0})
    //     .animate('#contact-background', { duration: 300, property:'opacity', start:0});

    // scrollorama
    //     .animate('#func-title',{ delay: 0, duration:300, property:'padding-top', start:0, pin:true })
    //     .animate('#soa-title',{ delay: 0, duration:300, property:'padding-top', start:0, pin:true })
    //     .animate('#smt-title',{ delay: 0, duration:300, property:'padding-top', start:0, pin:true })
    //     .animate('#team-title',{ delay: 0, duration:300, property:'padding-top', start:0, pin:true });

    onTeamImg();
});

function onTeamImg() {
    $('.team-member')
        .mouseover(function() {
        var order = $(this).attr('order');
        $('#team-mem-intro-' + order).css('opacity', 1);
        })
        .mouseout(function() {
            var order = $(this).attr('order');
            $('#team-mem-intro-' + order).css('opacity', 0);
        });

}
