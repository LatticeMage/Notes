# Flywheel

<iframe class="my-iframe" width="800" height="500" src="Diagram.drawio.html"></iframe>

<!-- prettier-ignore -->
<mermaid-renderer>
%% Code for flowchart below
graph TB
    subgraph Flywheel Effect
        yt((Youtube<br>Twitch))
        fan((Iron Fans))
        dc((Discord))
        game((Game Writing))
        pay{{Patreon}}
        learn((Learning<br>New Concept))
        yt -- value --> fan
        fan ==> pay
        dc ==> game
        game ==> learn
        learn ==> yt
        pay ==> dc

        update -.-> pay
        game -.-> yt
        game -.-> update      
        end
</mermaid-renderer>

<iframe class="my-iframe" width="400" height="600" src="Marketing Funnel.html"></iframe>