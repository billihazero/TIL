## 리스트 (List)

- 순서가 있는 선형 자료구조.
- LIST는 [1, 2, 3] , [2, 3, 1] 처럼 순서가 다르면 별개의 LIST가 된다. </br>
(SET은 순서에 상관없이 (1, 2, 3) = (2, 3, 1)이 같은 SET 이다.) </br>
- **ArrayList**와 **LinkedList**로 나뉜다.

### Array List란 ?
> 고정된 저장공간과 순차적인 데이터 저장

Array(배열)는 선언시에 size를 정하여 해당 size만큼의 연속된 메모리를 할당받아 데이터를 연속적/순차적으로 저장하는 자료구조이다.

#### direct(random) access
> array 첫 주소 + 4(n - 1)   /////int형 배열일 경우

- Array는 연속적/순차적으로 저장되어 있기 때문에 array의 첫 주소값만 알고 있다면 어떤 index에도 즉시 접근이 가능하다. 이것을 direct(random) access라고 한다.
- O(1) 의 시간복잡도를 갖는다.

#### Dynamic array
> array의 resizing과 doubling

- ArrayList에서 선언 시 정한 size보다 더 많은 데이터를 저장해야하는 경우, Dynamic array를 사용한다.
- 더 큰 배열을 생성하고, 기존에 있던 데이터를 옮기고 새로운 데이터를 추가한다. (= resizing)
- 보통 더 큰 배열을 생성할 때 기존 배열의 2배로 size를 설정한다. (= doubling)
- 기존에 있던 배열을 삭제한다.

### Linked List란 ?
> 물리적 비연속적, 논리적 연속적

Node라는 구조체가 연결되는 형식으로 데이터를 저장하는 자료구조 이다.
Node는 데이터값과 next node의 주소값을 저장한다. 
Linked List는 메모리상 물리적으로는 비연속적으로 저장이 되어있지만, 각각의 node가 next node의 메모리 주소값을 가리킴으로써 **논리적인 연속성**을 갖게된다.
